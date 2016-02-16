# Lingbib

Lingbib is a comprehensive, collaborative bibliographic database for linguistics.
It is intended to be used with [Biblatex][biblatex] and the [S&P implementation][uss-biblatex] of the [Unified Stylesheet for Linguistics][uss], but can also be used with other Biblatex styles.

This is the main repository, which hosts the source data and associated resources.


## Overview

Every linguist who is a user of LaTeX currently has to create and maintain their own bibliography.
It would be much more efficient if we could all contribute to and use a single, comprehensive bibliographic database for the field of linguistics.
This approach will also help maximize the accuracy of the data.

Unconventionally, the source data is maintained in [YAML][yaml] format using the Biblatex data model.
This makes the database exceptionally easy to manipulate programmatically compared to the idiosyncratic BibTeX format, and keeps the source truly human-readable and -writable, unlike XML and JSON.

The source data is then converted to a BibTeX `.bib` file, suitable for use with the state-of-the-art combination of [Biblatex][biblatex] and [Biber][biber].
In the future, it will also be available in legacy BibTeX format (for compatibility with the old `bibtex` program and `.bst` style files), and potentially others as well.

We are also in the process of developing a web interface for easy viewing, search, submission to, and editing of the database.


## Project Status

This project is currently in the alpha stage.
The database is small, and the web interface is not yet available.

The database schema for how Lingbib uses the Biblatex entry types and data fields is nearing completion, and public documentation will be available soon.
You can see the current status of the source data and how we generate the Biblatex/BIB release in the main branch of this repository.

Please note that the "command-line helper app" referenced in the wiki and held in [lingbib/lingbib-app][app] is **defunct**.
We had originally planned to develop a system for syncing the Lingbib database with a personal database for use with Jabref and other desktop reference managers, but this has been postponed indefinitely.


## How to Contribute

### Submitting database entries and revisions

The main way you can contribute to Lingbib is by submitting new entries and revisions to the bibliography file.
This can be done though GitHub until the Lingbib web interface is available.
Details on how to do this will be posted in the wiki soon.
In the meantime, would-be contributors should [get in contact](Contact and Support).

### Join the Team

We are currently looking for additional maintainers, and we expect this need to grow over time as the database gets larger. 
Helping to maintain Lingbib will mostly involve handling pull requests and issues regarding the content of the database.

We could also use help from technically-inclined invididuals in testing the database schema and developing the web interface.

If you are interested getting more closely involved, you should [get in touch](Contact and Support) with us.
We would greatly appreciate your help! :smile:


## Documentation

General documentation is available on the [Lingbib wiki][wiki].
Information relevant only to maintainers is stored directly in the repository.

**IMPORTANT**: the wiki is currently out-of-date due to the above-mentioned change of plans and continuing rapid development.
Please [get in contact](Contact and Support) for current information.


## Contact and Support

We have a Gitter chatroom where you can join our discussion about building and maintaining Lingbib.
Feel free to also just drop by and say *hi*!

[![Join the chat at https://gitter.im/lingbib/lingbib][gitter-badge]][gitter-chat]

You can also report specific problems and bugs, and suggest improvements via [GitHub issues][issues].

Finally, feel free to contact the Lingbib co-creators, [Adam and Kenneth][email], directly by email.


[app]: https://github.com/lingbib/lingbib-app
[biblatex]: https://www.ctan.org/pkg/biblatex
[biber]: http://biblatex-biber.sourceforge.net/
[email]: mailto:adam.liter@gmail.com,khanson679@gmail.com
[for-contributors]: https://github.com/lingbib/lingbib/wiki/For-contributors
[for-maintainers]: https://github.com/lingbib/lingbib/wiki/For-maintainers
[getting-started]: https://github.com/lingbib/lingbib/wiki/Getting-started
[git]: http://git-scm.com/
[gitter-chat]: https://gitter.im/lingbib/support?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge
[gitter-badge]: https://badges.gitter.im/Join%20Chat.svg
[issues]: https://github.com/lingbib/lingbib/issues
[uss-biblatex]: https://github.com/semprag/biblatex-sp-unified
[uss]: http://celxj.org/downloads/UnifiedStyleSheet.pdf
[wiki]: https://github.com/lingbib/lingbib/wiki
[yaml]: http://yaml.org/
