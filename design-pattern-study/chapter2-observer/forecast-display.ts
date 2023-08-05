import { Observer, DisplayElement } from './interface';
import { WeatherData } from './weather-data';
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

export class ForecastDisplay implements Observer, DisplayElement{
    temperatureForcast: Forecast;
    humidityForcast: Forecast;
    pressureForcast: Forecast;
    temperature: number;
    humidity: number;
    pressure: number;
    weatherData: WeatherData;
    constructor(weatherData: WeatherData) {
        this.temperatureForcast = new Forecast();
        this.humidityForcast = new Forecast();
        this.pressureForcast = new Forecast();
        this.temperature = 0;
        this.humidity = 0;
        this.pressure = 0;
        this.weatherData = weatherData;
        weatherData.registerObserver(this);
    }
    update(temperature: number, humidity: number, pressure: number) {
        this.temperature = this.temperatureForcast.forecast(temperature);
        this.humidity = this.humidityForcast.forecast(humidity);
        this.pressure = this.pressureForcast.forecast(pressure);
        this.display();
    }
    display() {
        console.log(`예보: 온도 ${this.temperature}도, 습도 ${this.humidity}%, 기압 ${this.pressure}`);
    }
}
