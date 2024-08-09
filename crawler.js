const SitemapGenerator = require('sitemap-generator');

// create generator
const generator = SitemapGenerator('https://ufscheduler.com/', {
  stripQuerystring: false,
  filepath: './sitemap.xml',
  maxDepth: 0,
  maxEntriesPerFile: 50000,
  userAgent: 'MyCrawler'
});

// register event listeners
generator.on('done', () => {
  console.log('Sitemap generated!');
});

generator.on('error', (error) => {
  console.error(error);
});

generator.on('add', (url) => {
  console.log('URL added: ', url);
});

// start the generator
generator.start();
