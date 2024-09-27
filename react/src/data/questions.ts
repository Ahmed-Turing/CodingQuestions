export type QuestionDescription = {
    id: 1 | 2 | 3;
    mainDescription: string;
    tasks: string[];
};

export const questions: QuestionDescription[] = [
    {
        id: 1,
        mainDescription: 'The "Add +1 later" button asynchronously updates the counter after a delay. There is a bug in this.',
        tasks: ['Find and fix the bug.', 'If you press the "Add +1 later" button first and then press the "Add +1" button right away, the counter should show 2.']
    },
    {
        id: 2,
        mainDescription: 'Two counters where each one increments at different intervals. The second counter does not increment; that is a bug.',
        tasks: ['Find and fix the bug.', 'Fix the counters so that they both increment at their specified interval.', 'Add styling to the counters.']
    },
    {
        id: 3,
        mainDescription: 'Bar chart that shows sum of well horizontal lengths by vintage year.',
        tasks: ['Add axes labels.', 'Fit in as many x-axis labels as we can view without overlap.', 'Allow the user to copy the horizontal length data. Right click on a bar should bring up the option for the user to copy the length.']
    }
];