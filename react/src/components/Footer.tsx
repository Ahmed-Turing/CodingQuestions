import styled from 'styled-components';

const FooterContainer = styled.footer`
    background-color: #282c34;
    padding: 10px;
    color: white;
    text-align: center;
    position: fixed;
    width: 100%;
    left: 0;
    bottom: 0;
`;

const Footer = () => {
    const currentYear = new Date().getFullYear();
    return (
        <FooterContainer>
            <p>&copy; {currentYear} Turing Analytics</p>
        </FooterContainer>
    );
};

export default Footer;