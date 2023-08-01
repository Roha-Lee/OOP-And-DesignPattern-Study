import { MallardDuck, RedheadDuck, RubberDuck } from "./duck.js"

const mallardDuck = new MallardDuck();
const redheadDuck = new RedheadDuck();
const rubberDuck = new RubberDuck();

const ducks = [mallardDuck, redheadDuck, rubberDuck];

ducks.forEach(duck => {
    duck.display();
    duck.quack();
    duck.swim();
    duck.fly();
    console.log("-----");
});