export interface FlyBehavior {
    fly(): void;
}

export class FlyWithWings implements FlyBehavior {
    fly() {
        console.log("날개로 날다!");
    }
}

export class FlyNoWay implements FlyBehavior {
    fly() {
        console.log("날 수 없다!");
    }
}
