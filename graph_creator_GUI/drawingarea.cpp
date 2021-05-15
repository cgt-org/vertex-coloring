#include <QSize>
#include <QPainter>
#include <QPaintEvent>
#include <QFileDialog>
#include <cmath>
#include <iostream>
#include <fstream>
#include "drawingarea.h"

DrawingArea::DrawingArea(QWidget *parent) : QWidget(parent)
{
    setAttribute(Qt::WA_StaticContents);
    setAttribute(Qt::WA_StyledBackground);
    QSize size = QSize(800, 600);
    QImage newImage(size, QImage::Format_RGB32);
    newImage.fill(qRgb(255,255,255));
    QPainter painter(&newImage);
    painter.drawImage(QPoint(0,0), newImage);
    image = newImage;
    current_mode = MODE::VERTEX;
    isDrawingEdge = false;
    VertexID = 0;
}

void DrawingArea::paintEvent(QPaintEvent *event){
    QPainter painter(this);
    QRect dirtyRect = event->rect();
    painter.drawImage(dirtyRect, image, dirtyRect);
}

double getDist(QPoint one, QPoint two){
    return sqrt((one.x() - two.x())*(one.x() - two.x()) +(one.y() - two.y())*(one.y() - two.y()));
}


void DrawingArea::mousePressEvent(QMouseEvent *event){
    QPoint pos = event->pos();
    if(current_mode == MODE::VERTEX){
        graph.append(Vertex(pos, VertexID));
        VertexID++;
    }else if(isDrawingEdge){
        double min_dist = 999999;
        int min_index = -1;
        for(int i=0; i<graph.length(); i++){
            if(getDist(pos, graph[i].pos) < min_dist){
                min_dist = getDist(pos, graph[i].pos);
                min_index = i;
            }
        }
        graph[min_index].addEdge(graph[drawnEdgeBegin]);
        graph[drawnEdgeBegin].addEdge(graph[min_index]);
        isDrawingEdge = false;
        drawnEdgeBegin = -1;

    }else{
        double min_dist = 999999;
        int min_index = -1;
        for(int i=0; i<graph.length(); i++){
            if(getDist(pos, graph[i].pos) < min_dist){
                min_dist = getDist(pos, graph[i].pos);
                min_index = i;
            }
        }
        if(min_index != -1){
            drawnEdgeBegin = min_index;
            isDrawingEdge = true;
        }

    }
    clearImage();
    drawSelf();
}

void DrawingArea::slotModeChanged(QString text){
    if(text == "Add Vertices"){
        current_mode = MODE::VERTEX;
    }else if(text == "Add Edges"){
        current_mode = MODE::EDGE;
    }
}

void DrawingArea::clearImage(){
    QSize newSize = QSize(800,600);
    QImage newImage(newSize, QImage::Format_RGB32);
    newImage.fill(qRgb(255, 255, 255));
    QPainter painter(&newImage);
    painter.drawImage(QPoint(0, 0), newImage);
    image = newImage;
    update();
}

void DrawingArea::drawSelf(){
    //first draw all the magical vertices
    QPainter painter(&image);
    QPen red(QColor(255,0,0));
    QPen green(QColor(0,255,0));
    QPen black(QColor(0,0,0));
    black.setWidth(3);
    red.setWidth(15);
    green.setWidth(15);
    painter.setPen(red);
    for(int i=0; i<graph.length(); i++){
        if(isDrawingEdge && i == drawnEdgeBegin){
            painter.setPen(green);
            painter.drawPoint(graph[i].pos);
            painter.setPen(red);
            continue;
        }
        painter.drawPoint(graph[i].pos);
    }
    painter.setPen(black);
    for(int i=0; i<graph.length(); i++){
        for(int j=0; j<graph[i].neighbours.length(); j++){
            painter.drawLine(graph[i].pos, graph[i].neighbours[j].pos);
        }
    }
}

void DrawingArea::slotSaveToFile(){
    QString fileName = QFileDialog::getSaveFileName(this,
                                                    tr("Save graph"), "",
                                                    tr("Graph Json file (*.json)"));
    std::ofstream file;
    file.open(fileName.toUtf8().constData());
    file << "{\n";
    for(int i=0; i<graph.length(); i++){
        file << "  \"" << graph[i].id << "\": [\n";
        for(int j = 0; j<graph[i].neighbours.length(); j++){
            file << "    \"" << graph[i].neighbours[j].id << "\"";
            if(j != graph[i].neighbours.length() - 1){
                file << ",";
            }
            file << "\n";
        }
        file << "  ]";
        if(i != graph.length() - 1){
            file << ",";
        }
        file << "\n";
    }
    file << "}\n";
    file.close();
}

void DrawingArea::slotNewFile(){
    graph.clear();
    isDrawingEdge = false;
    drawnEdgeBegin = -1;
    VertexID = 0;
    clearImage();
}
