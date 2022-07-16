clear
cd ../src
npm i axios express ghost-cursor puppeteer-extra-plugin-stealth puppeteer-extra https-proxy-agent axios-https-proxy-fix
npm i -g pm2
pm2 stop all
pm2 kill
pm2 start index.js --name "solver-node"
pm2 logs solver-node --lines 100