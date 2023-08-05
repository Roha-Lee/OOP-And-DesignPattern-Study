class Forecast {
    prevValue: number;
    currValue: number;
    constructor() {
        this.prevValue = 0;
        this.currValue = 0;
    }

    forecast(value: number) {
        const result = value + (this.currValue - this.prevValue);
        this.prevValue = this.currValue;
        this.currValue = result;
        return result;
    }
}

export class ForecastDisplay {
    temperatureForcast: Forecast;
    humidityForcast: Forecast;
    pressureForcast: Forecast;
    constructor() {
        this.temperatureForcast = new Forecast();
        this.humidityForcast = new Forecast();
        this.pressureForcast = new Forecast();
    }
    update(temperature: number, humidity: number, pressure: number) {
        const temperatureForcast = this.temperatureForcast.forecast(temperature);
        const humidityForcast = this.humidityForcast.forecast(humidity);
        const pressureForcast = this.pressureForcast.forecast(pressure);
        this.display(temperatureForcast, humidityForcast, pressureForcast);
    }
    display(temperatureForcast: number, humidityForcast: number, pressureForcast: number) {
        console.log(`예보: 온도 ${temperatureForcast}도, 습도 ${humidityForcast}%, 기압 ${pressureForcast}`);
    }
}
