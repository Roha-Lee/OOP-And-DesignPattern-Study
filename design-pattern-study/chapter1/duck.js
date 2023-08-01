export class Duck {
    constructor(type = "오리") {
        this.type = type;
    }
    quack() {
        console.log(`${this.type}: 꽥!`);
    }
    swim() {
        console.log(`${this.type}: 헤엄치기!`);
    }
    display() {
        console.log(`${this.type}`);
    }
    fly() {
        console.log(`${this.type}: 날다!`);
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
    }
    quack() {
        console.log(`${this.type}: 삑삑!`);
    }
}
