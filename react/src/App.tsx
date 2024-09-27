import styled from 'styled-components';
import Question3 from './components/Question3.tsx';
import Question1 from './components/Question1.tsx';
import Header from './components/Header';
import Footer from './components/Footer';
import { DataStructure } from './types.ts';
import jsonData from './data/data.json';
import React, { useState } from 'react';
import Question2 from './components/Question2.tsx';
import { questions, QuestionDescription } from './data/questions.ts';

const Container = styled.div`
    display: flex;
    flex-direction: column;
    padding: 20px;
    margin-top: 80px;
    align-items: center;
`;

const MainContent = styled.div`
    display: flex;
    width: 100%;
    max-width: 1200px;
    margin-top: 20px;
`;

const DescriptionContainer = styled.div`
    flex: 0 0 250px;
    padding: 20px;
    background: #f9f9f9;
    border-right: 1px solid #ccc;
    margin-right: 20px;
    border-radius: 8px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
`;

const QuestionContainer = styled.div`
    flex: 1;
    padding: 20px;
    background: #fff;
    border-radius: 8px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
`;

const DescriptionList = styled.ul`
    list-style-type: disc;
    padding-left: 20px;
`;

const ButtonContainer = styled.div`
    display: flex;
    justify-content: center;
    gap: 10px;
    margin-bottom: 20px;
    padding-top: 20px;
`;

const QuestionButton = styled.button`
    padding: 15px 20px;
    border: none;
    background-color: #007bff;
    color: white;
    border-radius: 5px;
    cursor: pointer;
    font-size: 18px;

    &:hover {
        background-color: #0056b3;
    }
`;

const App = () => {
    const [selectedQuestion, setSelectedQuestion] = useState<QuestionDescription | null>(null);

    const renderQuestion = () => {
        if (!selectedQuestion) {
            return <p>Select a question to begin.</p>;
        }

        let questionComponent;
        switch (selectedQuestion.id) {
            case 1:
                questionComponent = <Question1 />;
                break;
            case 2:
                questionComponent = <Question2 />;
                break;
            case 3:
                questionComponent = <Question3 data={data['all']} />;
                break;
            default:
                questionComponent = null;
        }

        return (
            <MainContent>
                <DescriptionContainer>
                    <h3>Description</h3>
                    <p>{selectedQuestion.mainDescription}</p>
                    <h3>Tasks</h3>
                    <DescriptionList>
                        {selectedQuestion.tasks.map((task, index) => (
                            <li key={index}>{task}</li>
                        ))}
                    </DescriptionList>
                </DescriptionContainer>
                <QuestionContainer>
                    {questionComponent}
                </QuestionContainer>
            </MainContent>
        );
    };

    const data: DataStructure = {
        all: jsonData,
        category1: jsonData.filter(item => item.value > 150),
        category2: jsonData.filter(item => item.value <= 150)
    };

    return (
        <React.Fragment>
            <Header />
            <Container>
                <ButtonContainer>
                    {questions.map((question) => (
                        <QuestionButton key={question.id} onClick={() => setSelectedQuestion(question)}>
                            Question {question.id}
                        </QuestionButton>
                    ))}
                </ButtonContainer>
                <div className="question-display">
                    {renderQuestion()}
                </div>
            </Container>
            <Footer />
        </React.Fragment>
    );
};

export default App;

