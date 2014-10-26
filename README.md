spawningtool
============

spawningpool is tools for analyzing StarCraft 2 Replays. It uses the data parsed by [sc2reader](https://github.com/GraylinKim/sc2reader) to make data available in a more human-digestable format.

Currently, spawningpool offers a basic parser for extracting build orders from replays. Our goal is to incorporate more sophisticated techniques from Artificial Intelligence to understand and classify these build orders.

Installation
============
From PyPi (mostly stable)
```bash
pip install spawningtool
```

From GitHub (less stable)
```bash
pip install -e git+git://github.com/StoicLoofah/spawningtool.git#egg=spawningtool
```

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

To execute it as a module from within your python project:     
1. Copy the second spawningtool folder ( the one that contains the __main__.py file) into your project. 
2. You could then use spawningtool to help you build a replay model

```python
import spawningtool
from spawningtool.parser import GameTimeline

class SpawningReplayModel(model.db.Model, model.Jsonifiable):
  """Represents the sc2 feed of build time events parsed from the spawningtool."""

  def loadRequestedReplay(self, filePath):
    result_replay = spawningtool.parser.parse_replay(filePath)
    return result_replay
```

Support
============
Please submit any issues you encounter to the [GitHub project](https://github.com/StoicLoofah/spawningtool/issues). You're also welcome to email Kevin directly at kevin@kevinleung.com.

Thanks To
============
* @hahnicity for all of the code cleanup. Previously, spawningtool was just a script. Thanks to his help, the code is actually readable and packaged for others to use and improve
* @GraylinKim for lots of support. Even before the project switched over to using [sc2reader](https://github.com/GraylinKim/sc2reader), he offered advice and tips on getting this project off the ground.
