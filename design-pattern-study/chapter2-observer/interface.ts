export interface DisplayElement {
    display(): void;
}

export interface Observer {
    update(ttemperatureemp: number, humidity: number, pressure: number): void;
}

export interface Subject {
    registerObserver(o: Observer): void;
    removeObserver(o: Observer): void;
    notifyObservers(): void;
}