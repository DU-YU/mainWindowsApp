#include "MainWindow.h"
#include "ui_MainWindow.h"

MainWindow::MainWindow(QWidget *parent) :
   QMainWindow(parent),
   ui(new Ui::MainWindow)
{
   ui->setupUi(this);
}

MainWindow::~MainWindow()
{
   delete ui;
}

void MainWindow::on_openFilePushButton_clicked()
{

}

void MainWindow::on_getHandlePushButton_clicked()
{

}

void MainWindow::on_startPushButton_toggled(bool checked)
{

}