import styled from 'styled-components';

const HeaderContainer = styled.header`
    background-color: #282c34;
    padding: 20px;
    color: white;
    text-align: center;
    width: 100%;
    position: fixed;
    top: 0;
    left: 0;
`;

const Header = () => {
    return (
        <HeaderContainer>
            <h1>React Coding Questions</h1>
        </HeaderContainer>
    );
};

export default Header;