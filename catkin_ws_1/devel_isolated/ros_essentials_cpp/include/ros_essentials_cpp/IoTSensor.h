// Generated by gencpp from file ros_essentials_cpp/IoTSensor.msg
// DO NOT EDIT!


#ifndef ROS_ESSENTIALS_CPP_MESSAGE_IOTSENSOR_H
#define ROS_ESSENTIALS_CPP_MESSAGE_IOTSENSOR_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace ros_essentials_cpp
{
template <class ContainerAllocator>
struct IoTSensor_
{
  typedef IoTSensor_<ContainerAllocator> Type;

  IoTSensor_()
    : id(0)
    , name()
    , temperature(0.0)
    , humidity(0.0)  {
    }
  IoTSensor_(const ContainerAllocator& _alloc)
    : id(0)
    , name(_alloc)
    , temperature(0.0)
    , humidity(0.0)  {
  (void)_alloc;
    }



   typedef int32_t _id_type;
  _id_type id;

   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _name_type;
  _name_type name;

   typedef float _temperature_type;
  _temperature_type temperature;

   typedef float _humidity_type;
  _humidity_type humidity;




  typedef boost::shared_ptr< ::ros_essentials_cpp::IoTSensor_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::ros_essentials_cpp::IoTSensor_<ContainerAllocator> const> ConstPtr;

}; // struct IoTSensor_

typedef ::ros_essentials_cpp::IoTSensor_<std::allocator<void> > IoTSensor;

typedef boost::shared_ptr< ::ros_essentials_cpp::IoTSensor > IoTSensorPtr;
typedef boost::shared_ptr< ::ros_essentials_cpp::IoTSensor const> IoTSensorConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::ros_essentials_cpp::IoTSensor_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::ros_essentials_cpp::IoTSensor_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace ros_essentials_cpp

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': False}
// {'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg'], 'actionlib_msgs': ['/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg'], 'ros_essentials_cpp': ['/home/pi/catkin_ws_1/src/ros_essentials_cpp/msg', '/home/pi/catkin_ws_1/devel_isolated/ros_essentials_cpp/share/ros_essentials_cpp/msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::ros_essentials_cpp::IoTSensor_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::ros_essentials_cpp::IoTSensor_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::ros_essentials_cpp::IoTSensor_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::ros_essentials_cpp::IoTSensor_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::ros_essentials_cpp::IoTSensor_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::ros_essentials_cpp::IoTSensor_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::ros_essentials_cpp::IoTSensor_<ContainerAllocator> >
{
  static const char* value()
  {
    return "16767b4b63fd3551b69c6c06672a0bf6";
  }

  static const char* value(const ::ros_essentials_cpp::IoTSensor_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x16767b4b63fd3551ULL;
  static const uint64_t static_value2 = 0xb69c6c06672a0bf6ULL;
};

template<class ContainerAllocator>
struct DataType< ::ros_essentials_cpp::IoTSensor_<ContainerAllocator> >
{
  static const char* value()
  {
    return "ros_essentials_cpp/IoTSensor";
  }

  static const char* value(const ::ros_essentials_cpp::IoTSensor_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::ros_essentials_cpp::IoTSensor_<ContainerAllocator> >
{
  static const char* value()
  {
    return "int32 id\n\
string name\n\
float32 temperature\n\
float32 humidity\n\
";
  }

  static const char* value(const ::ros_essentials_cpp::IoTSensor_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::ros_essentials_cpp::IoTSensor_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.id);
      stream.next(m.name);
      stream.next(m.temperature);
      stream.next(m.humidity);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct IoTSensor_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::ros_essentials_cpp::IoTSensor_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::ros_essentials_cpp::IoTSensor_<ContainerAllocator>& v)
  {
    s << indent << "id: ";
    Printer<int32_t>::stream(s, indent + "  ", v.id);
    s << indent << "name: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.name);
    s << indent << "temperature: ";
    Printer<float>::stream(s, indent + "  ", v.temperature);
    s << indent << "humidity: ";
    Printer<float>::stream(s, indent + "  ", v.humidity);
  }
};

} // namespace message_operations
} // namespace ros

#endif // ROS_ESSENTIALS_CPP_MESSAGE_IOTSENSOR_H
