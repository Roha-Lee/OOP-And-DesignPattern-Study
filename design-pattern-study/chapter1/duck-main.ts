import { ModelDuck } from "./duck-new"
import { FlyWithWings } from "./fly-behavior";
const modelDuck = new ModelDuck();

modelDuck.display();
modelDuck.quack();
modelDuck.fly();

modelDuck.setFlyBehavior(new FlyWithWings());

modelDuck.display();
modelDuck.quack();
modelDuck.fly();
