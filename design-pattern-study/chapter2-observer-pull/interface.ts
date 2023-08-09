export interface DisplayElement {
    display(): void;
}

export interface Observer {
    update(): void;
}

export interface Subject {
    registerObserver(o: Observer): void;
    removeObserver(o: Observer): void;
    notifyObservers(): void;
}