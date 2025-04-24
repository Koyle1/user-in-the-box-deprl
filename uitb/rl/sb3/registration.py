from gymnasium.envs.registration import register
import gymnasium as gym
import os

class Registration():
    def __init__(self, simulator):
        self.register_folder = "..../Registration"
        self.simulator = simulator
        self.id = ''
        self.entry_point = '' #Reference: my_custom_env.my_env:MyCustomEnv

    def _check_status(self):
        return False
    
    def _register(self):
        path = os.path.join(self.register_folder, self.id)      
        reg_config = f'''
        from gymnasium.envs.registration import register

        register(
            id="{self.id}",
            entry_point="{self.entry_point}",
        )
        '''
        file_path = f"{self.id}_register.py"  # You can change the path/name as needed
        with open(file_path, "w") as f:
            f.write(reg_config)
        print(f"Registration file written to {file_path}")
        

    def _make(self):
        try:
            if _check_status():
                _register()

            env = gym.make(self.id)
            return env

        except:
            print("Something went wrong during the building of your enviorment :(")
            retrun None
            
