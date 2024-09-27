import { useState } from 'react';
import styled from 'styled-components';

const Container = styled.div`
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 20px;
    max-width: 400px;
    margin: auto;
`;

const CountDisplay = styled.span`
    font-size: 24px;
    margin-bottom: 20px;
`;

const Button = styled.button`
    margin: 10px;
    padding: 10px 20px;
    border: none;
    background-color: #007bff;
    color: white;
    border-radius: 5px;
    cursor: pointer;
    font-size: 16px;

    &:hover {
        background-color: #0056b3;
    }
`;
export default function Question1() {
    const [count, setCount] = useState(0);

    const update = () => setCount(count + 1);

    // Update state after 2 seconds.
    const asyncUpdate = () => {
        setTimeout(() => {
            setCount(count + 1);
        }, 2000);
    };

    return (
        <Container>
            <CountDisplay>Count: {count}</CountDisplay>
            <Button onClick={update}>Add +1</Button>
            <Button onClick={asyncUpdate}>Add +1 later</Button>
        </Container>
    );
}