const { rot13 } = require('./transform');
const defaultInput = 'amber';
function render(input = defaultInput) {
  const transformed = rot13(input);
  return `r3:${transformed}`;
}
module.exports = { render };
