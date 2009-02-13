Summary:	A .NET framework for logging
Summary(pl.UTF-8):	Szkielet .NET do logowania
Name:		log4net
Version:	1.2.9
Release:	1
License:	Apache
Group:		Libraries
Source0:	http://cvs.apache.org/dist/incubator/log4net/1.2.9/incubating-%{name}-%{version}-beta.zip
# Source0-md5:	5c1526c8fdf78d6c33800cc7fbf78c6a
Source1:	%{name}.key
Source2:	%{name}.pc
URL:		http://logging.apache.org/log4net/
BuildRequires:	mono-csharp
BuildRequires:	unzip
%if "%(locale -a | grep -q '^en_US\.utf8$' ; echo $?)" == "1"
BuildRequires:	locale(en_US.utf8)
%endif
Conflicts:	pkgconfig < 1:0.19
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
log4net is a tool to help the programmer output log statements to a
variety of output targets. log4net is a port of the excellent log4j
framework to the .NET runtime.

%description -l pl.UTF-8
log4net to narzędzie pomagające programiście przekierowywać logi na
różne wyjścia. log4net to port świetnego szkieletu log4j do środowiska
uruchomieniowego .NET.

%prep
%setup -q -c

%build
export LC_CTYPE=en_US.UTF-8
mcs -out:log4net.dll \
	-keyfile:%{SOURCE1} \
	/target:library \
	/r:System.dll \
	/r:System.Data.dll \
	/r:System.Web.dll \
	src/Appender/AdoNetAppender.cs \
	src/Appender/AnsiColorTerminalAppender.cs \
	src/Appender/AppenderCollection.cs \
	src/Appender/AppenderSkeleton.cs \
	src/Appender/AspNetTraceAppender.cs \
	src/Appender/BufferingAppenderSkeleton.cs \
	src/Appender/BufferingForwardingAppender.cs \
	src/Appender/ColoredConsoleAppender.cs \
	src/Appender/ConsoleAppender.cs \
	src/Appender/DebugAppender.cs \
	src/Appender/EventLogAppender.cs \
	src/Appender/FileAppender.cs \
	src/Appender/ForwardingAppender.cs \
	src/Appender/IAppender.cs \
	src/Appender/LocalSyslogAppender.cs \
	src/Appender/MemoryAppender.cs \
	src/Appender/NetSendAppender.cs \
	src/Appender/OutputDebugStringAppender.cs \
	src/Appender/RemoteSyslogAppender.cs \
	src/Appender/RemotingAppender.cs \
	src/Appender/RollingFileAppender.cs \
	src/Appender/SmtpAppender.cs \
	src/Appender/SmtpPickupDirAppender.cs \
	src/Appender/TelnetAppender.cs \
	src/Appender/TextWriterAppender.cs \
	src/Appender/TraceAppender.cs \
	src/Appender/UdpAppender.cs \
	src/Config/AliasDomainAttribute.cs \
	src/Config/AliasRepositoryAttribute.cs \
	src/Config/BasicConfigurator.cs \
	src/Config/ConfiguratorAttribute.cs \
	src/Config/DomainAttribute.cs \
	src/Config/DOMConfigurator.cs \
	src/Config/DOMConfiguratorAttribute.cs \
	src/Config/Log4NetConfigurationSectionHandler.cs \
	src/Config/PluginAttribute.cs \
	src/Config/RepositoryAttribute.cs \
	src/Config/SecurityContextProviderAttribute.cs \
	src/Config/XmlConfigurator.cs \
	src/Config/XmlConfiguratorAttribute.cs \
	src/Core/CompactRepositorySelector.cs \
	src/Core/DefaultRepositorySelector.cs \
	src/Core/ErrorCode.cs \
	src/Core/IAppenderAttachable.cs \
	src/Core/IErrorHandler.cs \
	src/Core/IFixingRequired.cs \
	src/Core/ILogger.cs \
	src/Core/ILoggerWrapper.cs \
	src/Core/IOptionHandler.cs \
	src/Core/IRepositorySelector.cs \
	src/Core/ITriggeringEventEvaluator.cs \
	src/Core/Level.cs \
	src/Core/LevelCollection.cs \
	src/Core/LevelEvaluator.cs \
	src/Core/LevelMap.cs \
	src/Core/LocationInfo.cs \
	src/Core/LogException.cs \
	src/Core/LoggerManager.cs \
	src/Core/LoggerWrapperImpl.cs \
	src/Core/LoggingEvent.cs \
	src/Core/LogImpl.cs \
	src/Core/SecurityContext.cs \
	src/Core/SecurityContextProvider.cs \
	src/Core/WrapperMap.cs \
	src/DateFormatter/AbsoluteTimeDateFormatter.cs \
	src/DateFormatter/DateTimeDateFormatter.cs \
	src/DateFormatter/IDateFormatter.cs \
	src/DateFormatter/Iso8601DateFormatter.cs \
	src/DateFormatter/SimpleDateFormatter.cs \
	src/Filter/DenyAllFilter.cs \
	src/Filter/FilterDecision.cs \
	src/Filter/FilterSkeleton.cs \
	src/Filter/IFilter.cs \
	src/Filter/LevelMatchFilter.cs \
	src/Filter/LevelRangeFilter.cs \
	src/Filter/LoggerMatchFilter.cs \
	src/Filter/MdcFilter.cs \
	src/Filter/NdcFilter.cs \
	src/Filter/PropertyFilter.cs \
	src/Filter/StringMatchFilter.cs \
	src/Layout/Pattern/AppDomainPatternConverter.cs \
	src/Layout/Pattern/DatePatternConverter.cs \
	src/Layout/Pattern/ExceptionPatternConverter.cs \
	src/Layout/Pattern/FileLocationPatternConverter.cs \
	src/Layout/Pattern/FullLocationPatternConverter.cs \
	src/Layout/Pattern/IdentityPatternConverter.cs \
	src/Layout/Pattern/LevelPatternConverter.cs \
	src/Layout/Pattern/LineLocationPatternConverter.cs \
	src/Layout/Pattern/LoggerPatternConverter.cs \
	src/Layout/Pattern/MessagePatternConverter.cs \
	src/Layout/Pattern/MethodLocationPatternConverter.cs \
	src/Layout/Pattern/NamedPatternConverter.cs \
	src/Layout/Pattern/NdcPatternConverter.cs \
	src/Layout/Pattern/PatternLayoutConverter.cs \
	src/Layout/Pattern/PropertyPatternConverter.cs \
	src/Layout/Pattern/RelativeTimePatternConverter.cs \
	src/Layout/Pattern/ThreadPatternConverter.cs \
	src/Layout/Pattern/TypeNamePatternConverter.cs \
	src/Layout/Pattern/UserNamePatternConverter.cs \
	src/Layout/Pattern/UtcDatePatternConverter.cs \
	src/Layout/ExceptionLayout.cs \
	src/Layout/ILayout.cs \
	src/Layout/IRawLayout.cs \
	src/Layout/Layout2RawLayoutAdapter.cs \
	src/Layout/LayoutSkeleton.cs \
	src/Layout/PatternLayout.cs \
	src/Layout/RawLayoutConverter.cs \
	src/Layout/RawPropertyLayout.cs \
	src/Layout/RawTimeStampLayout.cs \
	src/Layout/RawUtcTimeStampLayout.cs \
	src/Layout/SimpleLayout.cs \
	src/Layout/XMLLayout.cs \
	src/Layout/XMLLayoutBase.cs \
	src/Layout/XmlLayoutSchemaLog4j.cs \
	src/ObjectRenderer/DefaultRenderer.cs \
	src/ObjectRenderer/IObjectRenderer.cs \
	src/ObjectRenderer/RendererMap.cs \
	src/Plugin/IPlugin.cs \
	src/Plugin/IPluginFactory.cs \
	src/Plugin/PluginCollection.cs \
	src/Plugin/PluginMap.cs \
	src/Plugin/PluginSkeleton.cs \
	src/Plugin/RemoteLoggingServerPlugin.cs \
	src/Repository/Hierarchy/DefaultLoggerFactory.cs \
	src/Repository/Hierarchy/Hierarchy.cs \
	src/Repository/Hierarchy/ILoggerFactory.cs \
	src/Repository/Hierarchy/Logger.cs \
	src/Repository/Hierarchy/LoggerKey.cs \
	src/Repository/Hierarchy/ProvisionNode.cs \
	src/Repository/Hierarchy/RootLogger.cs \
	src/Repository/Hierarchy/XmlHierarchyConfigurator.cs \
	src/Repository/IBasicRepositoryConfigurator.cs \
	src/Repository/ILoggerRepository.cs \
	src/Repository/IXmlRepositoryConfigurator.cs \
	src/Repository/LoggerRepositorySkeleton.cs \
	src/Util/PatternStringConverters/AppDomainPatternConverter.cs \
	src/Util/PatternStringConverters/DatePatternConverter.cs \
	src/Util/PatternStringConverters/EnvironmentPatternConverter.cs \
	src/Util/PatternStringConverters/IdentityPatternConverter.cs \
	src/Util/PatternStringConverters/LiteralPatternConverter.cs \
	src/Util/PatternStringConverters/NewLinePatternConverter.cs \
	src/Util/PatternStringConverters/ProcessIdPatternConverter.cs \
	src/Util/PatternStringConverters/PropertyPatternConverter.cs \
	src/Util/PatternStringConverters/RandomStringPatternConverter.cs \
	src/Util/PatternStringConverters/UserNamePatternConverter.cs \
	src/Util/PatternStringConverters/UtcDatePatternConverter.cs \
	src/Util/TypeConverters/BooleanConverter.cs \
	src/Util/TypeConverters/ConversionNotSupportedException.cs \
	src/Util/TypeConverters/ConverterRegistry.cs \
	src/Util/TypeConverters/EncodingConverter.cs \
	src/Util/TypeConverters/IConvertFrom.cs \
	src/Util/TypeConverters/IConvertTo.cs \
	src/Util/TypeConverters/IPAddressConverter.cs \
	src/Util/TypeConverters/PatternLayoutConverter.cs \
	src/Util/TypeConverters/PatternStringConverter.cs \
	src/Util/TypeConverters/TypeConverter.cs \
	src/Util/TypeConverters/TypeConverterAttribute.cs \
	src/Util/AppenderAttachedImpl.cs \
	src/Util/CompositeProperties.cs \
	src/Util/ContextPropertiesBase.cs \
	src/Util/CountingQuietTextWriter.cs \
	src/Util/CyclicBuffer.cs \
	src/Util/EmptyCollection.cs \
	src/Util/EmptyDictionary.cs \
	src/Util/FormattingInfo.cs \
	src/Util/GlobalContextProperties.cs \
	src/Util/LevelMapping.cs \
	src/Util/LevelMappingEntry.cs \
	src/Util/LogicalThreadContextProperties.cs \
	src/Util/LogLog.cs \
	src/Util/NativeError.cs \
	src/Util/NullDictionaryEnumerator.cs \
	src/Util/NullEnumerator.cs \
	src/Util/NullSecurityContext.cs \
	src/Util/OnlyOnceErrorHandler.cs \
	src/Util/OptionConverter.cs \
	src/Util/PatternConverter.cs \
	src/Util/PatternParser.cs \
	src/Util/PatternString.cs \
	src/Util/PropertiesDictionary.cs \
	src/Util/ProtectCloseTextWriter.cs \
	src/Util/QuietTextWriter.cs \
	src/Util/ReaderWriterLock.cs \
	src/Util/ReadOnlyPropertiesDictionary.cs \
	src/Util/ReusableStringWriter.cs \
	src/Util/SystemInfo.cs \
	src/Util/TextWriterAdapter.cs \
	src/Util/ThreadContextProperties.cs \
	src/Util/ThreadContextStack.cs \
	src/Util/ThreadContextStacks.cs \
	src/Util/Transform.cs \
	src/Util/WindowsSecurityContext.cs \
	src/AssemblyInfo.cs \
	src/AssemblyVersionInfo.cs \
	src/GlobalContext.cs \
	src/ILog.cs \
	src/LogicalThreadContext.cs \
	src/LogManager.cs \
	src/MDC.cs \
	src/NDC.cs \
	src/ThreadContext.cs

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/pkgconfig
cp %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/pkgconfig
gacutil -package log4net -gacdir %{_prefix}/lib -root $RPM_BUILD_ROOT%{_prefix}/lib -i log4net.dll > /dev/null

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_prefix}/lib/mono/gac/*
%{_prefix}/lib/mono/log4net
%{_datadir}/pkgconfig/log4net.pc
