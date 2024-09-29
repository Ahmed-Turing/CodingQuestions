import { useState, useEffect } from 'react';

export default function Question2() {

    const [count1, setCount1] = useState(0);
    const [count2, setCount2] = useState(0);

    useEffect(() => {
        const intervalId = setInterval(() => {
            setCount1(prevCount1 => prevCount1 + 1);
        }, 1000);

        return () => clearInterval(intervalId);
    }, []);

    useEffect(() => {
        const intervalId = setInterval(() => {
            setCount2(prevCount2 => prevCount2 + 1);
        }, 3000);

        return () => clearInterval(intervalId);
    }, []);

    return (
        <div className="App">
            <p>Counter 1 (1 sec): {count1}</p>
            <p>Counter 2 (3 sec): {count2}</p>
        </div>
    );
}