#ifndef UI_MAINWINDOW_H
#define UI_MAINWINDOW_H

#include <QMainWindow>

namespace Ui {
class MainWindow;
}

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

private slots:
    void on_openFilePushButton_clicked();

    void on_getHandlePushButton_clicked();

    void on_startPushButton_toggled(bool checked);

private:
    Ui::MainWindow *ui;
};

#endif // UI_MAINWINDOW_H
