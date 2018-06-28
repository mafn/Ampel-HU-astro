
from distutils.core import setup

setup(name='ampel-contrib-hu',
      version='0.2.0',
      packages=['ampel.contrib.hu',
                'ampel.contrib.hu.examples.t0',
                'ampel.contrib.hu.examples.t2',
                'ampel.contrib.hu.t0',
                'ampel.contrib.hu.t2',
                'ampel.contrib.hu.t3'],
      package_data = {'': ['*.json']},
      entry_points = {
          'ampel.channels' : [
              'hu = ampel.contrib.hu.channels:load_channels',
          ],
          'ampel.t2_run_configs' : [
              'hu = ampel.contrib.hu.channels:load_t2_run_configs',
          ],
          'ampel.pipeline.t0' : [
              'DecentFilter = ampel.contrib.hu.t0.DecentFilter:DecentFilter',
              'LensedTransientFilter = ampel.contrib.hu.t0.LensedTransientFilter:LensedTransientFilter',
              'NeutrinoFilter = ampel.contrib.hu.t0.NeutrinoFilter:NeutrinoFilter',
              'NoFilter = ampel.contrib.hu.t0.NoFilter:NoFilter',
              'RandFilter = ampel.contrib.hu.t0.RandFilter:RandFilter',
              'SEDmTargetFilter = ampel.contrib.hu.t0.SEDmTargetFilter:SEDmTargetFilter',
              'SNFilter = ampel.contrib.hu.t0.SNFilter:SNFilter',
              'TransientInEllipticalFilter = ampel.contrib.hu.t0.TransientInEllipticalFilter:TransientInEllipticalFilter',
          ],
          'ampel.pipeline.t2' : [
              'SNCOSMO = ampel.contrib.hu.t2.T2SNCosmo:T2SNCosmo',
              'POLYFIT = ampel.contrib.hu.examples.t2.T2ExamplePolyFit:T2ExamplePolyFit',
          ],
          'ampel.pipeline.t3.jobs' : [
              'hu = ampel.contrib.hu.channels:load_t3_jobs',
          ],
          'ampel.pipeline.t3.units' : [
              'TransientInfoPrinter = ampel.contrib.hu.t3.TransientInfoPrinter:TransientInfoPrinter',
              'SlackSummaryPublisher = ampel.contrib.hu.t3.SlackSummaryPublisher:SlackSummaryPublisher',
          ],
          'ampel.pipeline.t3.configs' : [
              'hu = ampel.contrib.hu.channels:load_t3_run_configs',
          ],
          'ampel.pipeline.resources' : [
              'extcats = ampel.contrib.hu.resources:extcatsURI',
              'catsHTM = ampel.contrib.hu.resources:catsHTMPath',
          ]
      }
)