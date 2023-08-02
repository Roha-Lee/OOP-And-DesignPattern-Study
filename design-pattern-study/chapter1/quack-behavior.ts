export interface QuackBehavior {
    quack(): void;
}

export class Quack implements QuackBehavior {
    quack() {
        console.log("꽥!");
    }
}

export class Squeak implements QuackBehavior {
    quack() {
        console.log("삑!");
    }
}

export class MuteQuack implements QuackBehavior {
    quack() {
        console.log("조용~");
    }
}
