import { useState, useEffect } from 'react';
import styled from 'styled-components';

const Container = styled.div`
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 100px;
    max-width: 400px;
    margin: auto;
`;

const CountDisplay = styled.span`
    font-size: 24px;
    margin-bottom: 20px;
`;


export default function Question2() {

    const [count1, setCount1] = useState(0);
    const [count2, setCount2] = useState(0);
    //counts were also stale and outdated
    //added empty dependency array to ensure the useEffects hooks run once
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
        <Container>
            <CountDisplay>Counter 1 (1 sec): {count1}</CountDisplay>
            <CountDisplay>Counter 2 (3 sec): {count2}</CountDisplay>
        </Container>
    );
}