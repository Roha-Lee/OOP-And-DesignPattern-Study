export class CurrentConditionsDisplay {
    update(temperature: number, humidity: number, pressure: number) {
        console.log(`현재 상태: 온도 ${temperature}도, 습도 ${humidity}%, 기압 ${pressure}`);
    }
}