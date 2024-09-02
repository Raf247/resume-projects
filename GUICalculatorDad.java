import javax.swing.*;
import java.awt.*;
import java.awt.Component;
import java.awt.FlowLayout;
import java.awt.event.ActionEvent; 
import java.awt.event.ActionListener;
import javax.swing.text.*;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;



public class GUICalculatorDad {
    public static void main(String[] args) {

        //SALARY variable
        final double SALARY = 17.00; 
        final int LUNCH_MINUTES = 30;

        // Create frame (window)
        JFrame frame = new JFrame("GUI Money Calculator");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(500, 500); 

        // Create panel
        JPanel panel = new JPanel();
        panel.setLayout(new BoxLayout(panel, BoxLayout.Y_AXIS));

        // Labels
        JLabel title = new JLabel("GUI Calculator", SwingConstants.CENTER);
        title.setAlignmentX(Component.CENTER_ALIGNMENT);
        panel.add(Box.createVerticalStrut(20));
        panel.add(title);
        panel.add(Box.createVerticalStrut(20));
        
        JLabel [] dayLabels = {new JLabel("Day 1 || "), new JLabel("Day 2 || "), new JLabel("Day 3 || "), new JLabel("Day 4 || "), new JLabel("Day 5 || "), new JLabel("Day 6 || ")};
        JLabel [] goIn = {new JLabel("In"), new JLabel("In"), new JLabel("In"), new JLabel("In"), new JLabel("In"), new JLabel("In")};
        JLabel [] goOut = {new JLabel("Out"), new JLabel("Out"), new JLabel("Out"), new JLabel("Out"), new JLabel("Out"), new JLabel("Out")};

        JLabel total = new JLabel("$0");

        // TextFields
        JTextField [] dayinFields = {new JTextField(10), new JTextField(10), new JTextField(10), new JTextField(10), new JTextField(10), new JTextField(10)};
        JTextField [] dayoutFields = {new JTextField(10), new JTextField(10), new JTextField(10), new JTextField(10), new JTextField(10), new JTextField(10)};

        // add time format to text fields
        for(JTextField field : dayinFields)
        {
            ((AbstractDocument) field.getDocument()).setDocumentFilter(new TimeformatFilter());
        }

        for(JTextField field : dayoutFields)
        {
            ((AbstractDocument) field.getDocument()).setDocumentFilter(new TimeformatFilter());
        }

        // create another panel to add to left and adds to main panel
        for (int i = 0; i < dayLabels.length; i++)
        {
            JPanel rowPanel = new JPanel(new FlowLayout(FlowLayout.LEFT));
            rowPanel.add(dayLabels[i]); //adds the labels
            rowPanel.add(goIn[i]);
            rowPanel.add(dayinFields[i]); //adds the correspondings text fields
            rowPanel.add(goOut[i]);
            rowPanel.add(dayoutFields[i]); //adds the correspondings text fields
            panel.add(rowPanel); //adds new panel to the main panel
        }

        // comboBox for lunch break
        JLabel lunchLabel = new JLabel("How many days of Lunch?");
        String [] lunchOptions = {"1", "2", "3", "4", "5", "6"};
        JComboBox<String> lunchComboBox = new JComboBox<>(lunchOptions);
        
        //making it smaller since it took the whole screen
        Dimension comboBoxSize = new Dimension(100, 20);
        lunchComboBox.setPreferredSize(comboBoxSize); // w: 60, h: 20
        lunchComboBox.setMaximumSize(comboBoxSize);

        JPanel rowPanel1 = new JPanel(new FlowLayout(FlowLayout.LEFT));
        rowPanel1.add(lunchLabel);
        rowPanel1.add(lunchComboBox);
        panel.add(rowPanel1);


        // Buttons
        JButton calculate = new JButton("Calculate");

        // Add an action listener to the button
        calculate.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                SimpleDateFormat format = new SimpleDateFormat("HH:mm");
                long totalMinutes = 0;

                for (int i = 0; i < dayinFields.length; i++)
                {
                    try {
                        String inTime = dayinFields[i].getText();
                        String outTime = dayoutFields[i].getText();
                        
                        if (!inTime.isEmpty() && !outTime.isEmpty())
                        {
                            Date inDate = format.parse(inTime);
                            Date outDate = format.parse(outTime);
                            
                            //calculate time difference in miliseconds
                            long difference = outDate.getTime() - inDate.getTime();

                            //converts it to min
                            long minutes = difference / (1000 * 60);
                            totalMinutes += minutes;
                        } 
                    } catch (ParseException ex)
                    {
                        //if the time is not correctly formatted then continue
                        continue;
                    }

                }

                //convert total minutes to hours and minutes
                double hours = totalMinutes / 60;
                double minutes = totalMinutes % 60;

                //calculates how much got paid
                double totalMoney = (double)(SALARY * hours) + ((SALARY / 60) * minutes);
                
                int lunchBreakDays = Integer.parseInt((String) lunchComboBox.getSelectedItem());
                double lunchDeduction = ((SALARY / 60) * LUNCH_MINUTES) * lunchBreakDays;

                totalMoney -= lunchDeduction;

                total.setText("Total: $" + String.format("%.2f", totalMoney));
            }
        });

        // Add the label and button to the panel
        panel.add(total);
        panel.add(Box.createVerticalStrut(20));
        panel.add(calculate);
        panel.add(Box.createVerticalStrut(20));

        // Add the panel to the frame
        frame.add(panel);

        // Make the frame visible
        frame.setVisible(true);
    }


}

class TimeformatFilter extends DocumentFilter
{
    @Override
    public void insertString(FilterBypass fb, int offset, String string, AttributeSet attr) throws BadLocationException
    {
        if (string == null) return;
        StringBuilder newString = new StringBuilder(fb.getDocument().getText(0, fb.getDocument().getLength()));
        newString.replace(offset, offset + length, text);
        if(isValidTimeFormat(newString.toString()))
        {
            super.replace(fb, offset, length, text, attrs);
        }
    }

    @Override
    public void replace(FilterBypass fb, int offset, int length, String text, AttributeSet attrs) throws BadLocationException {
        if (text == null) return;
        StringBuilder newString = new StringBuilder(fb.getDocument().getText(0, fb.getDocument().getLength()));
        newString.replace(offset, offset + length, text);
        if (isValidTimeFormat(newString.toString())) {
            super.replace(fb, offset, length, text, attrs);
        }
    }

    private boolean isValidTimeFormat(String text)
    {
        return text.matches("[0-2]?[0-9]?:?[0-5]?[0-9]?"); //allow partial time input (e.g., "12:", "12:3")
    }
}

//using this code make it so when the calculate button is clicked, it