import React, { PropsWithChildren, useState } from "react"

import './ContextMenu.module.css';

type Props = {
    id: string;
    items: ContextMenuItem[];
    onItemClicked: (item: ContextMenuItem) => void;
}

export type ContextMenuItem ={
    id: string;
    caption: string;
}

const ContextMenu = (props: PropsWithChildren<Props>) =>{
    const {items, children, id, onItemClicked} = props;

    const [isVisable, setIsVisable] = useState(false);

    const [position, setPosition] = useState<{x: number, y: number}>({
        x: 0,
        y: 0,
    });

    const contextMenuHandler = (e: React.MouseEvent) =>{
        e.preventDefault();
        setIsVisable(true);
        setPosition({x: e.clientX, y: e.clientY});
    }

    return (<>
        <div onContextMenu={contextMenuHandler}>{children}</div>
        {isVisable && 
            <ul className={`contextMenu`}
            style={{left: position.x, top: position.y}}
                
            >
                {items.map((item: ContextMenuItem) => (
                    <li 
                        key={item.id} 
                        onClick={() => {
                            setIsVisable(false);
                            onItemClicked(item);
                        }}
                    >
                        {item.caption}
                    </li>
                ))}    
        </ul>}
    </>
    );
};

export default ContextMenu;