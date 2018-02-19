Please update to Sass v3.5.2+.

    sudo apt-get install ruby
    sudo gem install sass
    sudo gem update sass

Download bootstrap sources:

    npm install bootstrap

Create file `custom.scss` with contents:

    $body-bg: #000;
    $body-color: #111;

    @import "node_modules/bootstrap/scss/bootstrap";

Then issue:

    scss custom.scss out.css

There you have it: `out.css` will contain customized Bootstrap.
