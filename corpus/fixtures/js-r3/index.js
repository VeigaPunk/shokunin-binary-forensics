const { rot13, checksum } = require('./transform');
const defaultInput = 'amber';
function render(input = defaultInput) {
  const transformed = rot13(input);
  return `r3:${transformed}:${checksum(transformed).toString(16).padStart(8, '0')}`;
}
module.exports = { render };
