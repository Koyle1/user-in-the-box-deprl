import os
import importlib
import numpy as np
import pathlib

import torch
import deprl

from deprl import custom_distributed
from deprl.utils import load_checkpoint, prepare_params
from deprl.vendor.tonic import logger

from ..base import BaseRLModel
from .callbacks import EvalCallback

from .registration import Registration



class Deprl(BaseRlModel):
    def __init__(self, simulator, checkpoint_path=None, wandb_id=None, info_keywords=()):
    super().__init__()

    rl_config = self.load_config(simulator)
    run_parameters = simulator.run_parameters
    simulator_folder = simulator.simulator_folder

    # Get total timesteps
    self.total_timesteps = rl_config["total_timesteps"]

    def load_config(self, simulator):
        pass

    def learn(self, wandb_callback, with_evaluation=False, eval_freq=400000, n_eval_episodes=5, eval_info_keywords=()):
        pass

    def _register_enviorment(self, simulator):
        '''
            Input: Simulator
            Output: Registrierung
            Description: 
        '''
        self.registrator = Registration(self.simulator)

    def load_config(self, simulator):
        pass

class Model():
    def __init__(self):
        pass