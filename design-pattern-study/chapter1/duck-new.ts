import { FlyBehavior, FlyWithWings, FlyNoWay } from "./fly-behavior";
import { QuackBehavior, Quack, Squeak } from "./quack-behavior";

export class Duck {
    type: String;
    flyBehavior: FlyBehavior;
    quackBehavior: QuackBehavior;
    constructor(type = "오리") {
        this.type = type;
        this.quackBehavior = new Quack();
        this.flyBehavior = new FlyNoWay();
    }
    setFlyBehavior(flyBehavior: FlyBehavior) {
        this.flyBehavior = flyBehavior;
    }

    setQuackBehavior(quackBehavior: QuackBehavior) {
        this.quackBehavior = quackBehavior;
    }

    quack() {
        this.quackBehavior.quack();
    }
    fly() {
        this.flyBehavior.fly();
    }
    swim() {
        console.log(`${this.type}: 헤엄치기!`);
    }
    display() {
        console.log(`${this.type}`);
    }
}

export class ModelDuck extends Duck {
    constructor() {
        super("모형오리");
    }
}
