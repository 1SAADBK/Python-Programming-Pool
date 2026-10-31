from ex0 import Creature
from ex1 import (HealingCreatureFactory,
                 TransformCreatureFactory,
                 HealCapability, TransformCapability)


if __name__ == "__main__":
    hf: HealingCreatureFactory = HealingCreatureFactory()
    hfb: Creature = hf.create_base()
    hfe: Creature = hf.create_evolved()
    print("Testing Creature with healing capability")
    if isinstance(hfb, HealCapability) and isinstance(hfe, HealCapability):
        print(" base:")
        print(hfb.describe())
        print(hfb.attack())
        print(hfb.heal())
        print(" evolved:")
        print(hfe.describe())
        print(hfe.attack())
        print(hfe.heal())
    tf: TransformCreatureFactory = TransformCreatureFactory()
    tfb = tf.create_base()
    tfe = tf.create_evolved()
    print("\nTesting Creature with transform capability")
    if (isinstance(tfb, TransformCapability)
            and isinstance(tfe, TransformCapability)):
        print(" base:")
        print(tfb.describe())
        print(tfb.attack())
        print(tfb.transform())
        print(tfb.attack())
        print(tfb.revert())
        print(" evolved:")
        print(tfe.describe())
        print(tfe.attack())
        print(tfe.transform())
        print(tfe.attack())
        print(tfe.revert())
