package example;

/* metamodel_version: 1.12.0 */
/* version: 1.0, 1.1-rc3 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  How a FIX datatype is written in another standard, such as XML Schema or protocol buffers.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OrchestraMappedDatatypeV11  {

  private OrchestraUnnamedEncodingV11 fixrEncoding;
  private OrchestraAnnotationV11 fixrAnnotation;
  private String fixrStandard;
  private Boolean fixrBuiltin;
  private String fixrBase;
  private String fixrPattern;
  private String fixrElement;
  private Integer fixrSize;
  private String fixrParameter;
  private String fixrMinInclusive;
  private String fixrMaxInclusive;


}