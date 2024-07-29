```swift

func handle(Request req) {
    if(req.type == 0){
        if(counter1 > 0){
            semaphore0.wait()
        }
        mutex0.wait()
        counter0++
        mutex0.signal()
        if(counter0 == 1){
            semaphore1.wait()
        }
        exec()
        mutex0.wait()
        counter0--
        mutex0.signal()
        if(counter0 == 0){
            semaphore1.signal()

        }
    }
    else{
        if(counter0 > 0){
            semaphore1.wait()
        }
        mutex1.wait()
        counter1++
        mutex1.signal()
        if(counter1 == 1){
            semaphore0.wait()
        }
        exec()
        mutex1.wait()
        counter1--
        mutex1.signal()
        if(counter1 == 0){
            semaphore0.signal()
        }        
    }
}

func main(){
    counter0 : number = 0
    counter1 : number = 1
    semaphore0 : Semaphore = Semaphore(1)
    semaphore1 : Semaphore = Semaphore(1)
    mutex0 : Semaphore = Semaphore(1)

}
```