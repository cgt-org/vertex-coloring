#ifndef VERTEX_H
#define VERTEX_H

#include <QVector>
#include <QPoint>

class Vertex
{
public:
    Vertex(QPoint p, int id);
    QVector<Vertex> neighbours;
    void addEdge(Vertex v);
    QPoint pos;
    int id;

};

#endif // VERTEX_H
