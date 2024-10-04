import React, { PropsWithChildren, useState, useEffect, useRef, } from "react"


type Props = {
    id: string;
    items: ContextMenuItem[];
    onItemClicked: (item: ContextMenuItem) => void;
}

export type ContextMenuItem ={
    id: string;
    caption: string;
}
//const ref = useRef<HTMLUListElement>(null);
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
/*
    const keyDownHandler = (e: KeyboardEvent) => {
        if(e.code == "Escape"){
            setIsVisable(false);
        }
    }*/
/*
    const clickHandler = (e: MouseEvent) => {
        if (isVisable){
            const rect = ref.current?.getBoundingClientRect();
            if(rect){
                if(e.clientX < rect.left || e.clientX > rect.right || e.clientY > rect.top || e.clientY < rect.bottom){
                    setIsVisable(false);
                }
            }
        }
    }
*/
/*
    useEffect( () => {
        window.addEventListener("keydown", keyDownHandler)

        return() => {
            window.removeEventListener("keydown", keyDownHandler);
        }

    }, [keyDownHandler]);
*/
    return (<>
        <div onContextMenu={contextMenuHandler}>{children}</div>
        {isVisable && 
            (<ul
            //ref={ref}
            className={`contextMenu`}
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
        </ul>)}
    </>
    );
};

export default ContextMenu;