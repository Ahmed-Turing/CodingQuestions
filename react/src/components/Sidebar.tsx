import styled from 'styled-components';

const SidebarContainer = styled.aside`
    width: 200px;
    background-color: #f4f4f4;
    padding: 20px;
    height: 100vh;
    position: fixed;
`;

const Sidebar = () => {
    return (
        <SidebarContainer>
            <ul>
                <li>Home</li>
                <li>About</li>
                <li>Contact</li>
            </ul>
        </SidebarContainer>
    );
};

export default Sidebar;