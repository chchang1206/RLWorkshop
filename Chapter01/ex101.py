# create Environment with step() and reset()

from typing import Tuple


class Environment(object):
    """
    constructor
    """

    def __init__(self):
        """

        :rtype: object
        """
        self._initial_state = 1
        self._allow_action = [0, 1]  # o: A, 1: B
        self._states = [1, 2, 3]
        self._current_state = self._initial_state

    def step(self, action: int) -> Tuple[int, int]:
        """
        Step function: compute the one-step dynamic from the given action.
        Args: action (int)
        Returns: the tuple current_state, reward.
        """
        # check if the action is allowed
        if action not in self._allow_action:
            raise ValueError("Action is not allowed. Must be in action space.")

        reward = 0
        if action == 0 and self._current_state == 1:
            self._current_state = 2
            reward = 1
        elif action == 1 and self._current_state == 1:
            self._current_state = 3
            reward = 10
        elif action == 0 and self._current_state == 2:
            self._current_state = 1
            reward = 0
        elif action == 1 and self._current_state == 2:
            self._current_state = 3
            reward = 1
        elif action == 0 and self._current_state == 3:
            self._current_state = 2
            reward = 0
        elif action == 1 and self._current_state == 3:
            self._current_state = 3
            reward = 10

        return self._current_state, reward


    def reset(self) -> int:
        """
        Reset the environment starting from the initial state.
        Returns:
            THe environment state after reset (initial state).
        """
        self._current_state = self._initial_state
        return self._current_state


env1 = Environment()
state = env1.reset()
actions = [0, 0, 1, 1, 0, 1]
print(f"Initial state is {state}")
for action in actions:
    next_state, reward = env1.step(action)
    print(f"From state {state} to state {next_state} with action {action}, reward: {reward}")
    state = next_state






