// datamodel specific includes
#include "ExampleWithARelation.h"
#include "ExampleWithARelationConst.h"
#include "ExampleWithARelationObj.h"
#include "ExampleWithARelationData.h"
#include "ExampleWithARelationCollection.h"
#include <iostream>
#include "ExampleWithNamespace.h"


namespace ex {

ConstExampleWithARelation::ConstExampleWithARelation() : m_obj(new ExampleWithARelationObj()){
 m_obj->acquire();
}



ConstExampleWithARelation::ConstExampleWithARelation(const ConstExampleWithARelation& other) : m_obj(other.m_obj) {
  m_obj->acquire();
}

ConstExampleWithARelation& ConstExampleWithARelation::operator=(const ConstExampleWithARelation& other) {
  if ( m_obj != nullptr) m_obj->release();
  m_obj = other.m_obj;
  return *this;
}

ConstExampleWithARelation::ConstExampleWithARelation(ExampleWithARelationObj* obj) : m_obj(obj){
  if(m_obj != nullptr)
    m_obj->acquire();
}

ConstExampleWithARelation ConstExampleWithARelation::clone() const {
  return {new ExampleWithARelationObj(*m_obj)};
}

ConstExampleWithARelation::~ConstExampleWithARelation(){
  if ( m_obj != nullptr) m_obj->release();
}

  const ex::ConstExampleWithNamespace ConstExampleWithARelation::ref() const { if (m_obj->m_ref == nullptr) {
 return ex::ConstExampleWithNamespace(nullptr);}
 return ex::ConstExampleWithNamespace(*(m_obj->m_ref));}


bool  ConstExampleWithARelation::isAvailable() const {
  if (m_obj != nullptr) {
    return true;
  }
  return false;
}

const podio::ObjectID ConstExampleWithARelation::getObjectID() const {
  if (m_obj !=nullptr){
    return m_obj->id;
  }
  return podio::ObjectID{-2,-2};
}

bool ConstExampleWithARelation::operator==(const ExampleWithARelation& other) const {
     return (m_obj==other.m_obj);
}

//bool operator< (const ExampleWithARelation& p1, const ExampleWithARelation& p2 ) {
//  if( p1.m_containerID == p2.m_containerID ) {
//    return p1.m_index < p2.m_index;
//  } else {
//    return p1.m_containerID < p2.m_containerID;
//  }
//}

} // namespace ex
