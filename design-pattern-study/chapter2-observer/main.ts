import { WeatherData } from './weather-data';
import { CurrentConditionsDisplay } from './current-conditions-display';    
import { StatisticsDisplay } from './statistics-display';
import { ForecastDisplay } from './forecast-display';
const weatherData = new WeatherData();

const currentConditionsDisplay = new CurrentConditionsDisplay(weatherData);
const statisticsDisplay = new StatisticsDisplay(weatherData);
const forecastDisplay = new ForecastDisplay(weatherData);

weatherData.setMeasurement(10, 20, 30);
weatherData.setMeasurement(11, 24, 50);
weatherData.setMeasurement(13, 23, 30);
weatherData.setMeasurement(11, 21, 20);
weatherData.setMeasurement(15, 20, 70);

