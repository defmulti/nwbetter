# PTHBetter #

## This is a fork of the original what.cd version with compatability for PTH ##

Introduction
------------

PTHBetter is a script which automatically transcodes and uploads FLACs
on PTH.

The following command will scan through every FLAC you have ever
downloaded, determine which formats are needed, transcode the FLAC to
each needed format, and upload each format to PTH -- automatically.

    $ pthbetter

Installation
------------

**IF YOU HAVE A PREVIOUS VERSION OF WHATBETTER OR PTHBETTER, YOU NEED TO REMOVE ALL FILE.**

*BE CAREFUL, ON PTH V2 IS TOLERATE ONLY IF V0 DOESN'T EXIST.
V2 IS TRUMPABLE WITH V0.
PLEASE DON'T ADD V2 ON YOUR CONFIG FILE.*

You're going to need to install a few dependencies before using
PTHBetter.

First and foremost, you will need Python 2.7 or newer.

Once you've got Python installed, you will need a few modules: mechanize,
mutagen, and requests. Try this as sudo/root:

    $ pip install -r requirements.txt
    
Or without sudo:

    $ pip install --user -r requirements.txt
    
Alternatively, if you have setuptools installed, you can do this (in the
source directory):

    $ python setup.py install

This should theoretically install all required dependencies
automatically.

Furthermore, you need several external programs: mktorrent, flac,
lame, and sox. The method of installing these programs varies
depending on your operating system, but if you're using something like
Ubuntu you can do this:

    # aptitude install flac lame sox

or

    # apt-get install flac lame sox
    
To install the lastest version of mktorrent, we need to remove the old version and clone the github repo in a dir and make / make install

With sudo:

    $ sudo apt-get purge mktorrent
    $ cd yourdir/
    $ git clone https://github.com/Rudde/mktorrent.git
    $ cd mktorrent/
    $ make
    $ sudo make install
    
Without sudo:

    $ cd yourdir
    $ git clone https://github.com/Rudde/mktorrent.git
    $ cd mktorrent
    $ make
    $ echo 'export PATH=<path to mktorrent folder here>:$PATH' >> ~/.bashrc; . ~/.bashrc

At this point you may execute the following command:

    $ pthbetter
    
or

    $ ./pthbetter

And you will receive a notification stating that you should edit the
configuration file `~/.pthbetter/config` (if you're lucky).

If you have an error, try to setup chmod 777 on all files, even may be directory

     $ chmod 777 *

Configuration
-------------

You've made it far! Congratulations. Open up the file
\~/.pthbetter/config in a text editor. You're going to see something
like this:

    [passtheheadphones]
    username =
    password = 
    data_dir =
    output_dir =
    torrent_dir =
    formats = flac, v0, 320,
    media = sacd, soundboard, web, dvd, cd, dat, vinyl, blu-ray

`username` and `password` are your PTH login credentials. 
`data_dir` is the directory where your downloads are stored. 
`output_dir` is the directory where your transcodes will be created. If
the value is blank, `data_dir` will be used.
`torrent_dir` is the directory where torrents should be created (e.g.,
your watch directory). `formats` is a list of formats that you'd like to
support (so if you don't want to upload V2, just remove it from this
list).
`media` is a list of lossless media types you want to consider for
transcoding. The default value is all PTH lossless formats, but if
you want to transcode only CD and vinyl media, for example, you would
set this to 'cd, vinyl'

You should end up with something like this:

    [passtheheadphones]
    username = RequestBunny
    password = clapton
    data_dir = /srv/downloads
    output_dir =
    torrent_dir = /srv/torrents
    formats = flac, v0, 320
    media = cd, vinyl, web

Alright! Now you're ready to use PTHBetter.

Usage
-----

    usage: pthbetter [-h] [-s] [--config CONFIG] [--cache CACHE]
                      [release_urls [release_urls ...]]

    positional arguments:
      release_urls     the URL where the release is located

    optional arguments:
      -h, --help       show this help message and exit
      -s, --single     only add one format per release (useful for getting unique
                       groups)
      --config CONFIG  the location of the configuration file (default:
                       ~/.pthbetter/config)
      --cache CACHE    the location of the cache (default: ~/.pthbetter/cache)

Examples
--------

You can turn pthbetter executable with the command:

    $ chmod +x pthbetter

To transcode and upload every FLAC you've every downloaded (this may
take a while):

    $ pthbetter

or

    $ ./pthbetter

To transcode and upload a specific release (provided you have already
downloaded the FLAC and it is located in your `data_dir`):

    $ pthbetter http://passtheheadphones.me/torrents.php?id=1000\&torrentid=1000000
or  $ pthbetter "http://passtheheadphones.me/torrents.php?id=1000&torrentid=1000000"
    
or

    $ ./pthbetter http://passtheheadphones.me/torrents.php?id=1000\&torrentid=1000000
or  $ ./pthbetter "http://passtheheadphones.me/torrents.php?id=1000&torrentid=1000000"

Note that if you specify a particular release(s), pthbetter will
ignore your configuration's media types and attempt to transcode the
releases you have specified regardless of their media type (so long as
they are lossless types).

---- 

ADDITIONAL INFORMATION
----------------------

If after this you have an issue to create torrent on ruTorrent, please check the file `/rutorrent/plugins/create/conf.php` and verify :
    
    $ $pathToCreatetorrent = '';

of, it's not working

    $pathToCreatetorrent = '/usr/local/bin/mktorrent';
