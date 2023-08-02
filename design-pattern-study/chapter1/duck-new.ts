import { FlyBehavior, FlyWithWings, FlyNoWay } from "./fly-behavior";
import { QuackBehavior, Quack, Squeak } from "./quack-behavior";

export class Duck {
    type: String;
    flyBehavior: FlyBehavior;
    quackBehavior: QuackBehavior;
    constructor(type = "오리") {
        this.type = type;
        this.quackBehavior = new Quack();
        this.flyBehavior = new FlyWithWings();
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

export class MallardDuck extends Duck {
    constructor() {
        super("청둥오리");
    }
}

export class RedheadDuck extends Duck {
    constructor() {
        super("빨간머리오리");
    }
}

export class RubberDuck extends Duck {
    constructor() {
        super("고무오리");
        this.quackBehavior = new Squeak();
        this.flyBehavior = new FlyNoWay();
    }
}
