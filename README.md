spawningtool
============

spawningtool is tools for analyzing StarCraft 2 Replays. It uses the data parsed by [sc2reader](https://github.com/ggtracker/sc2reader) to make data available in a more human-digestable format.

Currently, spawningtool offers a basic parser for extracting build orders from replays. Our goal is to incorporate more sophisticated techniques from Artificial Intelligence to understand and classify these build orders.

Installation
============
From PyPi (stable but often out of date for the latest patch)
```bash
pip install spawningtool
```

From GitHub (less stable but recommended)
```bash
pip install -e git+git://github.com/StoicLoofah/spawningtool.git#egg=spawningtool
```

Note that master usually requires sc2reader master, not the latest versioned release, so you will need to grab sc2reader from GitHub as well. Although it is less stable, it is recommended because the latest versions of both spawningtool and sc2reader are necessary to parse the most recent patches of StarCraft 2

Usage
============
To execute it directly from the command line
```bash
python -m spawningtool PATH/TO/REPLAY
```

To execute it from within python
```python
import spawningtool.parser
spawningtool.parser.parse_replay('PATH/TO/REPLAY')
```

For more notes, see the [GitHub wiki](https://github.com/StoicLoofah/spawningtool/wiki)

Support
============
Please submit any issues you encounter to the [GitHub project](https://github.com/StoicLoofah/spawningtool/issues). You're also welcome to email Kevin directly at kevin@kevinleung.com.

Thanks To
============
* @dsjoerg for many contributions to sc2reader and replay parsing as a whole through his work at ggtracker
* @hahnicity for all of the code cleanup. Previously, spawningtool was just a script. Thanks to his help, the code is actually readable and packaged for others to use and improve
* @GraylinKim for lots of support. Even before the project switched over to using [sc2reader](https://github.com/GraylinKim/sc2reader), he offered advice and tips on getting this project off the ground.
