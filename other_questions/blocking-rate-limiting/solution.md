```swift

func handle(Request req) {
    if(req.type == 0){
        mutex.wait()
        counter0 += 1
        mutex.signal()
    }
    if(req.type == 1){
        mutex.wait()
        counter1 += 1
        mutex.signal()
    }
    if(counter0 > 1){
        semaphore1.wait()
        exec(req)
        semaphore1.signal()
    }
    else if(counter1 > 1){
        semaphore0.wait()
        exec(requ)
        semaphore0.signal()
    }

}

func main(){
    counter0 : number = 0
    counter1 : number = 1
    mutex : Semaphore = Semaphore(1)

}
```