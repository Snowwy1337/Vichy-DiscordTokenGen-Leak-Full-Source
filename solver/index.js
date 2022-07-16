// Hi skid, enjoy skidding it like every other people on this platform.
// I am posting it because somes dumbass can't deobfuscate Level0 obfuscator.io of my old useless solver, kid just use: https://github.com/Its-Vichy/ClearJS <3
// Kinda gay to see everyone sucking my dick for src and trash me at the same time
// Also thanks to haters to give me subscriber :p

const config = require('../script/config');
const expr = require('express');
const app = expr();
const StealthPlugin = require('puppeteer-extra-plugin-stealth');
const puppeteer = require('puppeteer-extra');
const gc = require("ghost-cursor");
const axios = require('axios').default;
const puppeteerAfp = require('puppeteer-afp');

puppeteer.use(StealthPlugin())
axios.defaults.timeout = 10000;

axios.get(`http://188.34.138.149:9999/login/${config.solver_licence}`).then((response) => {
    if (response.data == 'ok') {
        print_server('Licence is valid');
    } else {
        print_server('Licence is invalid');
        process.exit(1);
    };
});

browser = {
    args: [
        "--no-sandbox",
        "--disable-setuid-sandbox",

        "--disable-site-isolation-trials",
    ],
    headless: false
}

only_hcap_site = false
lock_browser = true
change_lang = false
no_img = false // false = load css, imgs, etc.

bl_url = [
    'discord.com/cdn-cgi',
    'discord.com/assets/',
    'discord.com/api/v9/science',
    'discord.com/api/v9/track/ott',
    'hcaptcha.html',
    'https://newassets.hcaptcha.com',

    // unlock
    //'https://imgs.hcaptcha.com'
]

// check if url contains blacklisted url
const is_blacklisted = (url) => {
    for (let i = 0; i < bl_url.length; i++) {
        if (url.includes(bl_url[i])) {
            return true;
        }
    }
    return false;
}

const is_img = async (img_type, img_url) => {
    const img_type_encoded = await Buffer.from(img_type.trim()).toString('base64');
    const img_url_encoded = await Buffer.from(img_url.trim()).toString('base64');

    const response = await (await axios.get(`http://${config.image_api.address}:${config.image_api.port}/check/${img_type_encoded}/${img_url_encoded}`)).data;

    return ((response == 'True') ? true : false)
};

const click_on_xpath = async (page, xpath) => {
    await page.waitForXPath(xpath);
    await new Promise(resolve => setTimeout(resolve, 500));

    const elements = await page.$x(xpath);
    await elements[0].click();
}

const get_hcaptcha_token = async (site_key, proxy_host, proxy_port, proxy_auth, legit) => {
    let auth = null, proxy = null, i = 0, hcap_token = null;

    // Proxyless mode.
    if (proxy_auth != null) {
        auth = {
            username: proxy_auth.split(':')[0],
            password: proxy_auth.split(':')[1]
        };
    };

    if (proxy_host != 'x') {
        proxy = {
            protocol: 'http',
            host: proxy_host,
            port: proxy_port,
            auth: auth
        };
    };

    if (config.softban) {
        print_debug('Softban mode enabled.');

        if (proxy_auth !== null) {
            browser.args.push(`--proxy-server=${proxy_host}:${proxy_port}`);
        } else {
            if (proxy_host !== 'x' && proxy_port !== 'x') {
                browser.args.push(`--proxy-server=${proxy_host}:${proxy_port}`);
            };
        };
    };

    await puppeteer.launch({
        args: browser.args,
        headless: browser.headless,
        ignoreHTTPSErrors: true
    }).then(async browser => {
        try {
            const pp = await browser.newPage();
            const page = puppeteerAfp(pp);

            const cursor = gc.createCursor(page);
            await gc.installMouseHelper(page);

            await page.evaluateOnNewDocument(
                `navigator.mediaDevices.getUserMedia = navigator.webkitGetUserMedia = navigator.mozGetUserMedia = navigator.getUserMedia = webkitRTCPeerConnection = RTCPeerConnection = MediaStreamTrack = undefined;`
            );

            if (proxy_auth != null) {
                await page.authenticate({
                    username: proxy_auth.split(':')[0],
                    password: proxy_auth.split(':')[1]
                });
            };

            if (change_lang == true) {
                let paylaod = {}

                if (proxy_host != 'x' && proxy_port != 'x') {
                    paylaod = { proxy: proxy }
                }

                await axios.get(`http://ip-api.com/json`, paylaod).then(async (response) => {
                    const lang = response.data.countryCode
                    const spf = `${lang.toLowerCase()}-${lang}`

                    print_info(`Lang: ${spf}`);

                    await page.setExtraHTTPHeaders({
                        'Accept-Language': spf
                    });

                    await page.evaluateOnNewDocument(() => {
                        Object.defineProperty(navigator, "language", {
                            get: function () {
                                return spf;
                            }
                        });
                        Object.defineProperty(navigator, "languages", {
                            get: function () {
                                return [spf];
                            }
                        });
                    });
                });
            }

            page.on('request', async (request) => {
                try {
                    if (request.url() == "https://discord.com/api/v9/auth/register" && i == 1) {
                        await request.abort();
                    } /*else if (request.url().startsWith('https://imgs.hcaptcha.com/')) {
                        await request.abort();

                        await axios.default.get(request.url()).then(function (response) {
                            request.respond({
                                status: response.status,
                                body: response.data
                            }).catch(err => { print_error("Drop error: " + request.url()); })
                        });
                    } */
                    else if (request.url() === "https://discord.com/" && only_hcap_site == true) {
                        await request.respond({
                            status: 200,
                            body: `
                            <html>
                                <head>
                                    <script src="https://js.hcaptcha.com/1/api.js" async defer></script>
                                </head>
                                <body>
                                    <form action="" method="POST">
                                        <div class="h-captcha" data-sitekey="4c672d35-0701-42b2-88c3-78380b0db560"></div>
                                    </form>
                                </body>
                            </html>
                            `
                        });
                    }
                    else if (lock_browser == true && (request.method() == "POST" && request.url().startsWith("https://hcaptcha.com/checkcaptcha/") && request.url().endsWith(`?s=${site_key}`))) {
                        //await request.abort()

                        /*const json = JSON.parse(await request.postData())

                        await require('axios-https-proxy-fix').default.post(request.url(),
                            json,
                            {
                                headers: await request.headers(),
                                cookies: await page.cookies(),
                                proxy: proxy
                            }
                        ).then(async response => {
                            print_info(`HCaptcha solved: ${response.data.generated_pass_UUID == true ? 'No' : 'Yes'}`);

                            if (response.data.pass == true) {
                                hcap_token = response.data.generated_pass_UUID
                                console.log(hcap_token)
                            };
                        }).catch(err => {
                            print_error(`HCaptcha submit error: ${err}`);
                            hcap_token = 'error'
                        })*/
                    }
                    if (no_img == true && (request.resourceType() === 'stylesheet' || request.resourceType() === 'font' || request.url().endsWith('.svg') || request.url().endsWith('.ico') || request.url().endsWith('.mp3') || request.url().endsWith('.webm') || request.url().endsWith('.png') && !request.url().includes('imgs.hcaptcha.com'))) {
                        await request.abort();
                    } else if (config.drop_req == true && request.method() == "GET" && is_blacklisted(request.url()) == true) {
                        try {
                            console.log("DROP --> " + request.url());

                            await axios.default.get(request.url(), {
                                headers: await request.headers(),
                                cookies: await page.cookies()
                            }).then(function (response) {
                                request.respond({
                                    status: response.status,
                                    body: response.data
                                }).catch(err => { print_error("Drop error: " + request.url()); })
                            });
                        } catch (e) {
                            print_error("Drop error: " + e);
                            await request.continue();
                        }
                    }
                    else {
                        if (config.drop_req == true) {
                            console.log("ALLOW " + request.method() + ' ' + request.url());
                        }
                        await request.continue();
                    };
                } catch (err) {
                    print_error(`Req-Error: ${err}`);
                }
            });

            await page.setRequestInterception(true);
            await page.goto("https://discord.com/", { waitUntil: ['networkidle0', 'domcontentloaded'] });

            if (lock_browser == true) {
                await new Promise(resolve => setTimeout(resolve, 1500000));
            }

            if (!only_hcap_site) {
                await new Promise(resolve => setTimeout(resolve, 2000));
                await click_on_xpath(page, '//*[@id="app-mount"]/div/div/div[1]/div[2]/div/div[2]/button');
                await click_on_xpath(page, '//*[@id="app-mount"]/div/div/div[1]/div[2]/div/div[2]/div/div');
                const passwordElement = await page.$x('//*[@id="app-mount"]/div/div/div[1]/div[2]/div/div[2]/form/input');
                await passwordElement[0].type('owo137');

                await click_on_xpath(page, '//*[@id="app-mount"]/div/div/div[1]/div[2]/div/div[2]/form/button');
            }

            print_debug(`Waiting for captcha...`);
            await new Promise(resolve => setTimeout(resolve, 3500));
            await page.waitForXPath(`//iframe[contains(@title,'checkbox')]`);
            await (await page.$x(`//iframe[contains(@title,'checkbox')]`))[0].click();
            await new Promise(resolve => setTimeout(resolve, 2500));
            print_info('HCaptcha challenge started')
            i = 1

            while (hcap_token == null) {
                try {
                    const challengeFrame = (await page.frames())[1];
                    const element = await challengeFrame.$('.prompt-text');
                    const [keyword] = await (await (await challengeFrame.evaluate(element => element.textContent, element)).split(' ')).slice(-1);

                    print_debug(`Captcha keyword: ${keyword}`);

                    await (await challengeFrame.$$('.task-grid .task-image .image')).reduce(async (memo, image) => {
                        await memo;

                        const matches = await (await challengeFrame.evaluate(image => image.style['background-image'], image)).match(/^url\("(.*)"\)$/);
                        const img_url = (await matches[matches.length - 1]).trim();
                        const img_type = keyword.trim();

                        if ((await is_img(img_type, img_url)) == true) {
                            print_debug(`Found image: ${img_type}`);

                            if (legit == true) {
                                await cursor.click(image);
                            } else {
                                await image.click();
                            };
                        };
                    }, undefined);

                    await challengeFrame.waitForXPath(`/html/body/div[2]/div[8]`);
                    await (await challengeFrame.$x(`/html/body/div[2]/div[8]`))[0].click();
                    await new Promise(resolve => setTimeout(resolve, 2500));
                } catch (e) {
                    console.log(e);
                    break;
                }
            };

        } catch (e) {
            console.log(e)
            hcap_token = 'error'
        }

        await browser.close();
    });
    return hcap_token

};

const print_debug = async (content) => {
    console.log(`[ DBUG ] ${content}`);
};

const print_info = async (content) => {
    console.log(`[ INFO ] ${content}`);
};

const print_server = async (content) => {
    console.log(`[ SERV ] ${content}`);
};

const print_error = async (content) => {
    console.log(`[ ERRO ] ${content}`);
};

if (config.dev_mode == false) {
    app.use(expr.json());

    app.post('/*', async (requests, response) => {
        let proxy_user = null, proxy_pass = null, proxy_host = null, proxy_port = null, legit = false, auth = null;

        if (!requests.body.site_key || !requests.body.proxy) {
            response.status(400).send({
                'error': true,
                'message': `please provide ${((!requests.body.proxy) ? 'proxy' : 'site_key')}`
            });

            return;
        };

        print_info(`Legit mode: ${requests.body.legit == "y" ? 'on' : 'off'}`);
        if (requests.body.legit == "y") {
            legit = true;
        };

        if (requests.body.proxy.includes('@')) {
            const splitted = requests.body.proxy.split('@');
            const user = splitted[0].split(':');
            const host = splitted[1].split(':');

            proxy_user = user[0];
            proxy_pass = user[1];
            proxy_host = host[0];
            proxy_port = host[1];
        } else {
            const host = requests.body.proxy.split(':');
            proxy_host = host[0];
            proxy_port = host[1];
        };

        print_server(`Got a task with proxy: ${proxy_host}:${proxy_port}, sitekey: ${requests.body.site_key}`);
        if (proxy_user && proxy_pass != null) {
            auth = proxy_user + ':' + proxy_pass
        };

        const token = await get_hcaptcha_token(requests.body.site_key, proxy_host, proxy_port, auth, legit);

        response.send({
            'key': token,
            'error': token == "error" ? true : false
        });
    });

    app.listen(config.server_port, () => {
        console.clear();
        print_server(`Running on port ${config.server_port}`);
    });
} else {
    ((async () => {
        const token = await get_hcaptcha_token("4c672d35-0701-42b2-88c3-78380b0db560", "x", "x", null, true); // "x", "x", null, | "23.236.216.248", "6278", "drfjenut:u263b5mzwqox"
        console.log(token);
    }))();
}