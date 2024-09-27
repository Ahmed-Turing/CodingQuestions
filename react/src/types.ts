export type DataType = {
    name: string;
    value: number;
};

export type DataStructure = {
    all: DataType[];
    category1: DataType[];
    category2: DataType[];
};

export type TreeDataType = {
    title: string;
    key: string;
};

export type TreeFilterProps = {
    selectedKey: string;
    setSelectedKey: (key: string) => void;
};