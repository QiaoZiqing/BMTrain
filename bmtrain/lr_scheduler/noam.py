import math
from .warmup import WarmupLRScheduler

class Noam(WarmupLRScheduler):
    """
        After a warmup period during which performs :math:`\text{lr}=\text{start\_lr}\times \dfrac{\text{num\_iter}}{\text{warmup\_iter}^{3/2}}`,
        The decay period performs :math:`\text{lr}=\text{start\_lr}\times \dfrac{\text{1}}{\sqrt{\text{num\_iter}}}`
    """

    def get_lr_warmup(self, num_iter) -> float:
        return self.start_lr / math.sqrt(self.warmup_iter) * num_iter / self.warmup_iter
    
    def get_lr_decay(self, num_iter) -> float:
        return self.start_lr / math.sqrt(num_iter)
