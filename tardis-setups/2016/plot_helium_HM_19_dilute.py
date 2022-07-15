"""
Boyle et al. (2016) Figure 7 t_explosion=19 days recomb
==========================


Article: Boyle, Aoife, Sim, Stuart A., Hachinger, Stephan, et al. 2017, A&A,
“Helium in double-detonation models of type Ia supernovae” (`ADS Link`_).

Original Input Files: `YAML`_, `Model`_, `Abundance`_

Original Atomic Dataset: Data present

Original Spectra: Data missing

Notes: Please note that the spectra obtained below is obtained by using a slightly
modified configuration file. This is done to ensure that the spectra can be
obtained using the computers hosted by us.

.. _ADS Link: https://ui.adsabs.harvard.edu/abs/2017A&A...599A..46B
"""


from tardis import run_tardis
from tardis.io.config_reader import Configuration
from tardis.io.atom_data.util import download_atom_data
import matplotlib.pyplot as plt

import sys

sys.path.append("../")
from setup_utils import config_modifier

# %%
conf = Configuration.from_yaml(
    "../../2016/2016_aoife_sim_kerzendrof/helium_HM_19_dilute.yml"
)

# %%
# Note: Here the configuration is slightly modified to allow
# the configuration file on a computer with lower configuration.

conf = config_modifier(conf)
# %%
sim = run_tardis(conf)


spectrum = sim.runner.spectrum
spectrum_virtual = sim.runner.spectrum_virtual
spectrum_integrated = sim.runner.spectrum_integrated

plt.figure(figsize=(10, 6.5))

spectrum.plot(label="Normal packets")
spectrum_virtual.plot(label="Virtual packets")
spectrum_integrated.plot(label="Formal integral")

plt.xlim(500, 9000)
plt.title("TARDIS example model spectrum")
plt.xlabel("Wavelength [$\AA$]")
plt.ylabel("Luminosity density [erg/s/$\AA$]")
plt.legend()
plt.show()
