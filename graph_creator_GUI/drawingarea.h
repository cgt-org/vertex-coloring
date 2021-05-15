#ifndef DRAWINGAREA_H
#define DRAWINGAREA_H

#include <QObject>
#include <QWidget>
#include <QVector>

#include "vertex.h"

class DrawingArea : public QWidget
{
    Q_OBJECT
public:
    explicit DrawingArea(QWidget *parent = nullptr);
    enum MODE{
        VERTEX,
        EDGE
    };

public slots:
    void slotModeChanged(QString string);
    void slotSaveToFile();
    void slotNewFile();

protected:
    void paintEvent(QPaintEvent *event) override;
    void mousePressEvent(QMouseEvent *event) override;

private:
    MODE current_mode;
    QImage image;
    QVector<Vertex> graph;

    void drawSelf();
    void clearImage();
    bool isDrawingEdge;
    int drawnEdgeBegin;
    int VertexID;
};

#endif // DRAWINGAREA_H
