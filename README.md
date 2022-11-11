# nagle

This is a reference implementation of [John F. Nagle](https://www.cmu.edu/physics/people/faculty/nagle.html)'s method for measuring redistricting bias & responsiveness and a code companion to his [whitepaper](http://lipid.phys.cmu.edu/nagle/Technical/2019-04-19%20-%20Measuring%20Redistricting%20Bias%20&%20Responsiveness.pdf) which describes the method.

You have successfully replicated his basic method, if you can take the information in in [Attachment 1](https://github.com/alecramsay/nagle/blob/master/attachments/1%20-%20VPI%20by%20Distrct.txt) and produce the outputs in [Attachment 2](https://github.com/alecramsay/nagle/blob/master/attachments/2%20-%20Inferred%20D%20S(V)%20Points.txt) and [Attachment 3](https://github.com/alecramsay/nagle/blob/master/attachments/3%20-%20Analytics.txt).

The [example file](https://github.com/alecramsay/nagle/blob/master/examples/PA-SCOPA-7S.py) does that, using the code in this repository within a Python environment.

The [examples directory](https://github.com/alecramsay/nagle/tree/master/examples) also contains pairs of files that define maps for PA, MD, and MA which can be analyzed at a command-line using the [analyze_plan.py script](https://github.com/alecramsay/nagle/blob/master/scripts/analyze_plan.py).

This repository also supports the paper @alecramsay helped John Nagle write in Election Law Journal, “On Measuring Two-Party Partisan Bias in Unbalanced States.” 

## License

Distributed under the [The MIT License (MIT)](https://github.com/alecramsay/nagle/blob/master/LICENSE) Copyright © 2018–2021 Alec Ramsay
